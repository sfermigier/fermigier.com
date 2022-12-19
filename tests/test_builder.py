from fermigier_com.builder import Builder


def test_builder():
    builder1 = Builder()
    builder2 = Builder()
    assert builder1.posts is not builder2.posts

    builder1.posts.append({})
    builder2.posts.append({1: 2})
    assert builder1 != builder2
