import pyray as rl


class OTFBMTextureContext:
    """
    Context for render textures. Acts as a way to wrap being_texture_mode and end_texture_mode. If other
    backends are implemented, then this will also act as a context manager for those.
    """

    def __enter__(self) -> rl.RenderTexture:
        # TODO: make dis shit
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        # TODO: make dis shit
        pass

    pass


class OTFBMImageContext:
    pass



