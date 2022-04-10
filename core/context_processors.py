from core.models import WebsiteSettings, HeaderFields

def header_footer_context(request):
    context = {
        "website": WebsiteSettings.objects.last(),
        "header": HeaderFields.items.active().order_by("order"),
        "footer": HeaderFields.items.footer().order_by("order"),

    }

    return context