from flask_dance.contrib.github import make_github_blueprint, github
from flask_dance.consumer import OAuth2ConsumerBlueprint


def test_blueprint_factory():
    github_bp = make_github_blueprint(
        client_id="foo",
        client_secret="bar",
        scope="user:email",
        redirect_to="index",
    )
    assert isinstance(github_bp, OAuth2ConsumerBlueprint)
    assert github_bp.session.scope == "user:email"
    assert github_bp.session.base_url == "https://api.github.com/"
    assert github_bp.session.client_id == "foo"
    assert github_bp.client_secret == "bar"
    assert github_bp.authorization_url == "https://github.com/login/oauth/authorize"
    assert github_bp.token_url == "https://github.com/login/oauth/access_token"