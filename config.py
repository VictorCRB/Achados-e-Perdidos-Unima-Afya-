"""
config.py — Configurações globais do Achados Unima Afya

Define cores da identidade visual da Afya (magenta), fontes,
tamanhos e a chave da API ImgBB.
"""

# ============================================
# IDENTIDADE VISUAL — CORES OFICIAIS DA AFYA
# ============================================
COLORS = {
    # Magenta — cor principal da Afya Unima
    "magenta": "#E6007E",
    "magenta_dark": "#B30062",
    "magenta_light": "#FF4DA6",
    "magenta_50": "#FDF2F8",
    "magenta_100": "#FCE7F3",

    # Tons de cinza
    "ink_900": "#0A0A0B",
    "ink_700": "#27272A",
    "ink_500": "#52525B",
    "ink_400": "#71717A",
    "ink_300": "#A1A1AA",
    "ink_200": "#D4D4D8",
    "ink_100": "#E4E4E7",
    "ink_50": "#F4F4F5",
    "ink_25": "#FAFAFA",
    "white": "#FFFFFF",

    # Status
    "status_aberto_bg": "#F4F4F5",
    "status_aberto_fg": "#52525B",
    "status_analise_bg": "#FEF3C7",
    "status_analise_fg": "#92400E",
    "status_encontrado_bg": "#DBEAFE",
    "status_encontrado_fg": "#1E40AF",
    "status_devolvido_bg": "#D1FAE5",
    "status_devolvido_fg": "#065F46",
    "status_naoachado_bg": "#FEE2E2",
    "status_naoachado_fg": "#991B1B",

    # Outros
    "success": "#10B981",
    "warning": "#F59E0B",
    "danger": "#EF4444",
}

# ============================================
# FONTES
# ============================================
FONTS = {
    "title_xl": ("Segoe UI", 28, "bold"),
    "title_lg": ("Segoe UI", 22, "bold"),
    "title_md": ("Segoe UI", 18, "bold"),
    "title_sm": ("Segoe UI", 16, "bold"),
    "body_lg": ("Segoe UI", 14),
    "body_md": ("Segoe UI", 13),
    "body_sm": ("Segoe UI", 12),
    "body_xs": ("Segoe UI", 11),
    "label": ("Segoe UI", 12, "bold"),
}

# ============================================
# CATEGORIAS DE ITENS
# ============================================
CATEGORIAS = [
    {"id": 1, "nome": "Material escolar", "icone": "📚"},
    {"id": 2, "nome": "Eletrônicos", "icone": "🎧"},
    {"id": 3, "nome": "Roupas", "icone": "👕"},
    {"id": 4, "nome": "Documentos", "icone": "💳"},
    {"id": 5, "nome": "Acessórios", "icone": "🔑"},
    {"id": 6, "nome": "Garrafas/Recipientes", "icone": "💧"},
    {"id": 7, "nome": "Outros", "icone": "📦"},
]

# ============================================
# LOCAIS DO CAMPUS
# ============================================
LOCAIS = [
    "Bloco A — Salas 101 a 120",
    "Bloco B — Laboratórios",
    "Bloco C — Salas 201 a 220",
    "Cantina principal",
    "Biblioteca",
    "Auditório",
    "Estacionamento",
    "Pátio central",
    "Não tenho certeza",
]

# ============================================
# STATUS POSSÍVEIS
# ============================================
STATUS = {
    "aberto": "Aberto",
    "analise": "Em análise",
    "encontrado": "Encontrado",
    "devolvido": "Devolvido",
    "naoachado": "Não encontrado",
}

# ============================================
# API IMGBB
# ============================================
# Para upload real de imagens, coloque aqui sua API key gratuita
# Crie em: https://api.imgbb.com (após criar conta em imgbb.com)
# Se deixar vazio, o sistema funciona em modo offline (sem upload real)
IMGBB_API_KEY = ""

# ============================================
# CONFIGURAÇÕES DA JANELA
# ============================================
APP_TITLE = "Achados Unima Afya"
APP_WIDTH = 1200
APP_HEIGHT = 760
APP_MIN_WIDTH = 1000
APP_MIN_HEIGHT = 650
