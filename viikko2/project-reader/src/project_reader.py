from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        parsed_content = toml.loads(content)["tool"]["poetry"]

        title = parsed_content["name"]
        description = parsed_content["description"]
        license = parsed_content["license"]

        authors = [i for i in parsed_content["authors"]]
        dependencies = [i for i in parsed_content["dependencies"]]
        group_dev_dependencies = [i for i in parsed_content["group"]["dev"]["dependencies"]]
        
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(title, description, license, authors, dependencies, group_dev_dependencies)
