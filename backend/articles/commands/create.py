from articles.dao import ArticleDAO
class CreateArticleCommand():

    def __init__(self, data):
        self._properties= data.copy()

    def run(self):
        self.validate()
        article= ArticleDAO.create(self.properties)
        return article

    def validate():
        pass