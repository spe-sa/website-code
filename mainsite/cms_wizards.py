from cms.wizards.wizard_base import Wizard
from cms.wizards.wizard_pool import wizard_pool

from .forms import ArticleCreationForm
from spe_blog.models import Article

class ArticleCreationWizard(Wizard):
    pass

article_wizard = ArticleCreationWizard(
    title="New Article",
    weight=200,
    form=ArticleCreationForm,
    description="Create an article",
)

wizard_pool.register(article_wizard)
