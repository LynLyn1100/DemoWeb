from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.forms import modelform_factory, widgets
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = _('Tên người dùng')
        self.fields['password'].label = _('Mật khẩu')
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Đăng nhập'))
        self.helper.layout = Layout(
            Field('username', css_class='form-control'),
            Field('password', css_class='form-control'),
)
from django.shortcuts import render
from django.contrib.auth import views as auth_views

def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            # Xử lý đăng nhập thành công
            return HttpResponseRedirect(reverse('base'))  # Thay 'home' bằng url của trang chuyển hướng sau khi đăng nhập thành công
    else:
        form = CustomAuthenticationForm()
    return render(request, 'registration/login.html', {'custom_form': form})


# Create your views here.

from django.utils.translation import gettext_lazy as _

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = _('Tên người dùng')
        self.fields['password1'].label = _('Mật khẩu')
        self.fields['password2'].label = _('Xác nhận mật khẩu')

class Register(SuccessMessageMixin, generic.CreateView):
    form_class = CustomUserCreationForm  # Thay đổi từ UserCreationForm sang CustomUserCreationForm
    success_message = "Đăng ký thành công, bây giờ bạn có thể đăng nhập."
    template_name = "registration/register.html"
    success_url = reverse_lazy('login')

class CustomUserEditForm(modelform_factory(get_user_model(), fields=('email','first_name', 'last_name', 'username'))):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = _('Họ')
        self.fields['last_name'].label = _('Tên')
        self.fields['username'].label = _('Tên người dùng')
        self.fields['email'].label = _('Email')

@login_required
def profile(req):
    form = CustomUserEditForm(instance=req.user)
    if req.method == "POST":
        form = CustomUserEditForm(instance=req.user, data=req.POST)
        if form.is_valid():
            form.save()
    return render(req, 'registration/profile.html', {'form': form})

def contact(req):
    form = CustomUserEditForm(instance=req.user)
    if req.method == "POST":
        form = CustomUserEditForm(instance=req.user, data=req.POST)
        if form.is_valid():
            form.save()
    return render(req, 'registration/contact.html', {'form': form})
