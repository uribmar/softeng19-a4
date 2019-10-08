import pytest
from pathlib import Path
from pmgr.project import Project, TaskException

@pytest.fixture(scope="function")
def initialize_project():
    proj = Project("proj")
    yield proj
    dirpath = Path.cwd() / ".projects"
    filepath = dirpath / "proj.txt"
    filepath.unlink()
    dirpath.rmdir()
    del proj
    del filepath
    del dirpath

def test_project_init(initialize_project):
    proj = initialize_project
    assert(proj.name == "proj")

#TODO
def test_project_add(initialize_project):
    proj = initialize_project
    print(proj.name)
    pass

#TODO
def test_project_add_fail():
    pass

#TODO
def test_project_remove():
    pass

#TODO
def test_project_remove_fail():
    pass

#TODO
def test_project_get():
    pass
