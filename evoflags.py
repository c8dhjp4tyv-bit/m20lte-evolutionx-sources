import sys

gms = (sys.argv[1] if len(sys.argv) > 1 else "true") == "true"
p = "lineage_m20lte.mk"
s = open(p).read()
start, end = "# Evolution X flags (begin)\n", "# Evolution X flags (end)\n"
if start in s:
    s = s[:s.index(start)] + s[s.index(end) + len(end):]
block = start + f"""WITH_GMS := {'true' if gms else 'false'}
TARGET_USES_PICO_GAPPS := true
TARGET_BOOT_ANIMATION_RES := 1080
TARGET_HAS_UDFPS := false
TARGET_SUPPORTS_QUICK_TAP := false
EVO_BUILD_TYPE := Unofficial
PRODUCT_SYSTEM_PROPERTIES += ro.evolution.maintainer=umutcagand
""" + end
# flags must be set before the common config is inherited
anchor = "$(call inherit-product, vendor/lineage/config/common_full_phone.mk)"
assert anchor in s, "common_full_phone inherit not found"
s = s.replace(anchor, block + anchor, 1)
open(p, "w").write(s)
