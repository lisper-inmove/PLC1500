"""专机."""

from .auto_fill_ammo import auto_fill_ammo_bp
from .depth_test import depth_test_bp
from .engine_dismantle import engine_dismantle_bp
from .firebox_tighten import firebox_tighten_bp
from .long_tail_tighten import long_tail_tighten_bp

__all__ = [
    auto_fill_ammo_bp,
    depth_test_bp,
    engine_dismantle_bp,
    firebox_tighten_bp,
    long_tail_tighten_bp,
]
