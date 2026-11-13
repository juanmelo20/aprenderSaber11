"""Acceso a Firebase (Auth y Firestore). Funciona igual contra los emuladores y contra producción."""
from __future__ import annotations

import datetime as dt
import json
from functools import lru_cache

import firebase_admin
from firebase_admin import auth as fb_auth
from firebase_admin import credentials
from google.auth.credentials import AnonymousCredentials
from google.cloud import firestore

from .config import settings


@lru_cache
def _app() -> firebase_admin.App:
    if settings.service_account_json:
        cred = credentials.Certificate(json.loads(settings.service_account_json))
        return firebase_admin.initialize_app(cred, {"projectId": settings.project_id})
    return firebase_admin.initialize_app(options={"projectId": settings.project_id})


@lru_cache
def db() -> firestore.Client:
    _app()
    if settings.emulators or not settings.service_account_json:
        return firestore.Client(project=settings.project_id, credentials=AnonymousCredentials())
    info = json.loads(settings.service_account_json)
    return firestore.Client.from_service_account_info(info, project=settings.project_id)


def auth():
    _app()
    return fb_auth


def now() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


def clean(value):
    """Convierte fechas a ISO para poder devolver documentos como JSON."""
    if isinstance(value, dict):
        return {k: clean(v) for k, v in value.items()}
    if isinstance(value, list):
        return [clean(v) for v in value]
    if isinstance(value, dt.datetime):
        return value.isoformat()
    return value
