#jetsadaphon bokprakhon 653380014-1 sec.1
#Lab8

import pytest
from fastapi.testclient import TestClient
from main import Borrowlist, get_db, User, Book, app

@pytest.fixture
def client(db_session):
    def override_get_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db
    return TestClient(app)

@pytest.mark.parametrize("book_id",[1,2,3])
def test_CreateAndAccess_Borrowlist(client, db_session, book_id):
    #defining user
    user = User(username="CoolUsers!")
    db_session.add(user)
    db_session.commit()

    #requesting post from /borrowlist
    response = client.post(f"/borrowlist/?user_id={user.id}&book_id{book_id}")

    assert response.status_code == 200

    assert response.json()["book_id"] == book_id

    assert db_session.query(Borrowlist).filter_by(book_id=book_id).first()


