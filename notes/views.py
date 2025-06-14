
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Note, NoteVersion, Folder
from .forms import RegisterForm, NoteForm, FolderForm
from django.http import HttpResponse, HttpResponseForbidden  # ← 自動整合進現有 import


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('note_list')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def note_list(request):
    folder_id = request.GET.get('folder')
    folders = Folder.objects.filter(owner=request.user)
    if folder_id:
        notes = Note.objects.filter(owner=request.user, folder_id=folder_id)
    else:
        notes = Note.objects.filter(owner=request.user)
    others_notes = Note.objects.filter(is_public=True).exclude(owner=request.user).order_by('-updated_at')[:10]
    return render(request, 'notes/note_list.html', {
    'notes': notes,
    'folders': folders,
    'selected_folder': folder_id,
    'others_notes': others_notes,
})

    folders = Folder.objects.filter(owner=request.user)
    return render(request, 'notes/note_list.html', {'notes': notes, 'folders': folders})


@login_required
def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)

    if note.owner != request.user and not note.is_public:
        return HttpResponseForbidden("你無法查看這篇私人筆記。")

    return render(request, 'notes/note_detail.html', {'note': note})
   

@login_required
def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.owner = request.user
            note.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {
        'form': form,
        'note': None,
        'user': request.user,
        'is_create': True  
    })






@login_required
def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk)

    if note.owner != request.user and not note.editable:
        return HttpResponseForbidden("你沒有權限編輯這篇筆記。")

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note, user=request.user)
        if form.is_valid():
            updated_note = form.save(commit=False)
            NoteVersion.objects.create(note=note, content=note.content)

            if note.owner == request.user:
                updated_note.is_public = form.cleaned_data.get('is_public', note.is_public)
                updated_note.editable = form.cleaned_data.get('editable', note.editable)
            else:
                updated_note.is_public = note.is_public
                updated_note.editable = note.editable

            updated_note.save()
            return redirect('note_detail', pk=note.pk)
    else:
        form = NoteForm(instance=note)

    return render(request, 'notes/note_form.html', {
        'form': form,
        'note': note,
        'user': request.user,
        'is_create': True
    })
       


@login_required
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk, owner=request.user)
    if request.method == 'POST':
        note.delete()
        return redirect('note_list')
    return render(request, 'notes/note_confirm_delete.html', {'note': note})

@login_required
def search_notes(request):
    query = request.GET.get('q')
    notes = Note.objects.filter(owner=request.user)
    if query:
        keywords = query.split()
        for kw in keywords:
            notes = notes.filter(content__icontains=kw)
    return render(request, 'notes/note_list.html', {'notes': notes})

@login_required
def note_versions(request, pk):
    note = get_object_or_404(Note, pk=pk)

    if note.owner != request.user and not note.editable:
        return HttpResponseForbidden("你沒有權限查看這篇筆記的編輯紀錄。")

    versions = NoteVersion.objects.filter(note=note).order_by('-saved_at')
    return render(request, 'notes/note_versions.html', {'note': note, 'versions': versions})




@login_required
def folder_create(request):
    if request.method == 'POST':
        form = FolderForm(request.POST)
        if form.is_valid():
            folder = form.save(commit=False)
            folder.owner = request.user
            folder.save()
            return redirect('note_list')
    else:
        form = FolderForm()
    return render(request, 'notes/folder_form.html', {'form': form})


@login_required
def folder_list(request):
    folders = Folder.objects.filter(owner=request.user)
    return render(request, 'notes/folder_list.html', {'folders': folders})

@login_required
def folder_delete(request, pk):
    folder = get_object_or_404(Folder, pk=pk, owner=request.user)
    if request.method == 'POST':
        folder.delete()
        return redirect('folder_list')
    return render(request, 'notes/folder_confirm_delete.html', {'folder': folder})


@login_required
def note_clone(request, pk):
    original = get_object_or_404(Note, pk=pk, is_public=True, editable=True)
    cloned = Note.objects.create(
        title = original.title + "（複製）",
        content = original.content,
        folder = None,
        owner = request.user,
        is_public = False,
        editable = False,
    )
    return redirect('note_detail', pk=cloned.pk)
