from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'hostel'

urlpatterns = [
    path('', views.index, name='index'),
    path('allocations/<int:pk>', views.allocation_view, name='allocations'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('update/<int:pk>', views.update, name='update'),
    path('add/', views.add, name='add'),
    path('addroom/', views.addRoom, name='addroom'),
    path('deleteroom/<int:pk>', views.deleteRoom, name='deleteroom'),

    # ---------------- Password Reset ----------------
    # 🔑 User reset request
    path(
        "password-reset/user/",
        views.user_password_reset,
        name="user_password_reset"
    ),

    # 🔑 Admin reset request (with secret ID check)
    path(
        "password-reset/admin/",
        views.admin_password_reset,
        name="admin_password_reset"
    ),

    # ✅ Shared confirm + done (Django built-ins)
path(
    "reset/<uidb64>/<token>/",
    views.user_password_reset_confirm,
    name="password_reset_confirm"
),


    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="hostel/password_reset_done.html"
        ),
        name="password_reset_done"
    ),
]
