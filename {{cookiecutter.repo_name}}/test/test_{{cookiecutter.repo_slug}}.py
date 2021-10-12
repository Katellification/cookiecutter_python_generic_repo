from {{cookiecutter.repo_slug}} import {{cookiecutter.repo_slug}}


def test_fib() -> None:
    assert {{cookiecutter.repo_slug}}.fib(0) == 0
    assert {{cookiecutter.repo_slug}}.fib(1) == 1
    assert {{cookiecutter.repo_slug}}.fib(2) == 1
    assert {{cookiecutter.repo_slug}}.fib(3) == 2
    assert {{cookiecutter.repo_slug}}.fib(4) == 3
    assert {{cookiecutter.repo_slug}}.fib(5) == 5
    assert {{cookiecutter.repo_slug}}.fib(10) == 55
