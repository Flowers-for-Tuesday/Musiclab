from manim import VGroup
import inspect

def vrange(prefix, start, end):
    '''
    快捷调用相同前缀名变量，使用示例
    self.play(FadeOut(vrange("text", 1, 10)))
    '''
    ns = inspect.currentframe().f_back.f_locals
    return VGroup(*[ns[f"{prefix}{i}"] for i in range(start, end + 1)])