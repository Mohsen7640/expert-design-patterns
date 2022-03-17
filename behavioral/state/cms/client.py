from behavioral.state.crm.context.post import Post


def run():
    post = Post(pk=1, title="sample title", content="sample content")
    post.moderation()
    post.published()
    post.moderation()


if __name__ == '__main__':
    run()
