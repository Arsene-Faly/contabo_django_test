from django.urls import path

from blog.view.main_view import (
    home_view,
    service_view,
    about_view,
    blog_view,
    blog_detail_view,
)

from blog.view.auth_view import (
    login_view,
    register_view,
    logout_view,
)

from blog.view.admin_view import (
    admin_view,
)

from blog.view.article_view import (
    article_index_view,
    article_create_view,
    article_edit_view,
    article_delete_view,
    article_detail_view
)

from blog.view.category_view import (
    category_index_view,
    category_create_view,
    category_edit_view,
    category_delete_view,
    category_detail_view
)

urlpatterns = [
    # =========================
    # Site public
    # =========================
    path("", home_view, name="home"),
    path("services/", service_view, name="services"),
    path("about/", about_view, name="about"),
    path("blog/", blog_view, name="blog"),
    path("blog/detail/", blog_detail_view, name="blog_detail"),
    # =========================
    # Authentification
    # =========================
    path("auth/login/", login_view, name="login"),
    path("auth/register/", register_view, name="register"),
    path("auth/logout/", logout_view, name="logout"),
    # =========================
    # Administration
    # =========================
    path("admin_index/", admin_view, name="admin_dashboard"),
    # Articles
    path("admin_articles/", article_index_view, name="article_index"),
    path("admin_articles/create/", article_create_view, name="article_create"),
    path("admin_articles/detail/<int:id>/", article_detail_view, name="article_detail"),
    path("admin_articles/<int:id>/edit/", article_edit_view, name="article_edit"),
    path("admin_articles/<int:id>/delete/", article_delete_view, name="article_delete"),
    # Catégories
    path("admin_categories/", category_index_view, name="category_index"),
    path("admin_categories/detail/<int:id>/", category_detail_view, name="category_detail"),
    path("admin_categories/create/", category_create_view, name="category_create"),
    path("admin_categories/edit/<int:id>/", category_edit_view, name="category_edit"),
    path("admin_categories/delete/<int:id>/", category_delete_view, name="category_delete",),
]
