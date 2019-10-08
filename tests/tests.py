import pytest
from pathlib import Path
from pmgr.project import Project, TaskException


@pytest.fixture(scope="function")
def init_proj():
    proj = Project("proj")
    yield proj
    dirpath = Path.cwd() / ".projects"
    filepath = dirpath / "proj.txt"
    filepath.unlink()
    dirpath.rmdir()
    del proj
    del filepath
    del dirpath


@pytest.fixture(scope="function")
def init_proj_with_task(init_proj):
    proj = init_proj
    proj.add_task("task1")
    proj.add_task("task2")
    yield proj


def test_project_init(init_proj):
    proj = init_proj
    assert proj.name == "proj"
    projdir = Path.cwd() / ".projects"
    projfile = projdir / "proj.txt"
    assert projdir.is_dir()
    assert projfile.exists()


def test_project_add(init_proj):
    proj = init_proj
    proj.add_task("task1")
    projfile = Path.cwd() / ".projects/proj.txt"
    with open(str(projfile), 'r') as rf:
        lines = rf.readlines()
        assert len(lines) == 1
        assert lines[0].strip() == "task1"


def test_project_add_fail(init_proj):
    proj = init_proj
    proj.add_task("task1")
    with pytest.raises(TaskException):
        proj.add_task("task1")


def test_project_remove(init_proj_with_task):
    proj = init_proj_with_task
    proj.remove_task("task1")
    projfile = Path.cwd() / ".projects/proj.txt"
    with open(str(projfile), 'r') as rf:
        lines = rf.readlines()
        assert len(lines) == 1
        assert lines[0].strip() == 'task2'


def test_project_remove_fail(init_proj):
    proj = init_proj
    with pytest.raises(TaskException):
        proj.remove_task("task1")


def test_project_get(init_proj_with_task):
    proj = init_proj_with_task
    tasks = proj.get_tasks()
    assert len(tasks) == 2
    assert tasks[0] == 'task1'
    assert tasks[1] == 'task2'
