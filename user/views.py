from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login


from .forms import SignUpForm


def register(request):
    if request.method == 'POST':
        query_dict = request.POST.copy()
        query_dict['username'] = query_dict['email']
        form = SignUpForm(query_dict)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.newsletter = form.cleaned_data.get('newsletter')
            user.save()
            login(request, user)
            return redirect('user:userinfo')
    else:
        form = SignUpForm()
    return render(request, 'user/register.html', {'form': form})


@login_required(login_url='/login')
def user_info(request):
    return render(request, 'user/userinfo.html', {'user': request.user})
