"""
Django settings for config project.

Atualizado para deploy no Render
"""

from pathlib import Path
import dj_database_url
from decouple import config

# Diretório base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Segurança
SECRET_KEY = config("SECRET_KEY")  # pega do Environment Variable
DEBUG = config("DEBUG", default=False, cast=bool)

# Render exige que o domínio esteja no ALLOWED_HOSTS
ALLOWED_HOSTS = [
    "instituto-arion.onrender.com",  # domínio do Render
    "localhost",                     # útil para testes locais
]

# Aplicativos instalados
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Apps do projeto
    "voluntarios",
    "praticantes",
    "instituto",
]

# Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

# Templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # pasta templates global
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# Banco de dados (Render usa DATABASE_URL)
DATABASES = {
    "default": dj_database_url.config(
        default=config("DATABASE_URL")
    )
}

# Validação de senha
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internacionalização
LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_TZ = True

# Arquivos estáticos (CSS, JS)
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",  # pasta static global
]
STATIC_ROOT = BASE_DIR / "staticfiles"  # necessário para Render coletar

# Arquivos de mídia (imagens, uploads)
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Campo padrão para chaves primárias
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"