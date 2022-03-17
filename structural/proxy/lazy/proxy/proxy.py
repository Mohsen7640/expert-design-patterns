class LazyLoaderProxy:

    def __init__(self, cls):
        self.cls = cls
        self.instance = None

    def __getattr__(self, name):
        if self.instance is None:
            self.instance = self.cls()
        return getattr(self.instance, name)
