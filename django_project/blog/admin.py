from django.contrib import admin
# from .models import Post

# admin.site.register(Post)
from .models import FypaperPdf
admin.site.register(FypaperPdf)

from .models import FybookPdf
admin.site.register(FybookPdf)

from .models import SypaperPdf
admin.site.register(SypaperPdf)

from .models import SybookPdf
admin.site.register(SybookPdf)

from .models import TypaperPdf
admin.site.register(TypaperPdf)

from .models import TybookPdf
admin.site.register(TybookPdf)