import warnings
import pkg_resources

version = pkg_resources.get_distribution("vizblend").version

if version < "2.0.0":
    warnings.warn(
        f"🚨 VizBlend version {version} is deprecated! Please upgrade to version 2.0.0\n"
        "👉 Run pip install vizblend --upgrade vizblend",
        DeprecationWarning,
        stacklevel=2,
    )
