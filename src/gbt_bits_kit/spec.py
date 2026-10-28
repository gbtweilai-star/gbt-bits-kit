"""The capability contract, copied verbatim from the GBT V8 registry.

Do not hand-edit: ``tests/test_spec.py`` pins every field against the
registry snapshot so drift fails the build instead of shipping quietly.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Any, Dict, List, Tuple

_RAW = r"""{
 "name": "bits_kit",
 "domain": "creation",
 "desc": "**动效组件图鉴的口**（人话 → react-bits 哪个组件 · 干什么 · **源码在哪 · 会不会联网 · 依赖什么**）。素材：`DavidHDev/react-bits`（**MIT + Commons Clause v1.0** · ★49005 · 216 组件 · 5 类：Animations 39 / Backgrounds 62 / Components 48 / Micro 34 / TextAnimations 33）落 `_upstream/react-bits`。常用说法：动画 / 背景 / 文字动画 / 微交互 / 手风琴 / 画廊 / 卡片 / 光标跟随 / 粒子 / 网格 / 渐变 / 流光 / 毛玻璃 / 滚动 / 计数 / 故障 / 极光 / 波浪 / 液态 / 三维 / 音频 / 拖拽 / 轮播 / 开关 / 加载 / 翻牌 / 解密 / 描边 / 磁性。op=status/build/find/api/where：`build` 扫 `src/content`（**盘上目录是真相**）提 名·类目·说明（取自官方 `public/llms.txt`）·源码路径·注册表·依赖·**联网标**，落 `store/bits_kit/index.jsonl`（只追加），并把「清单与盘上对不上的地方」如实带出来；`find` 人话取候选（**命中 0 就是 0**，可 `only_offline=true` 只看不联网的）；`api` 按准确名取一条。🔴 铁律：**只读 · 零执行 · 不搬成品**（许可禁止再分发/移植）· **不碰 `public/rbp/**`**（付费版 Pro）· **不改 `_upstream/react-bits/**` 一个字节** · 说明只取原文，取不到留空。",
 "handler": "bits_kit",
 "safe": true,
 "external": false,
 "requires_params": false,
 "params": [],
 "params_hint": "",
 "multi_op": true,
 "ops": [
  "status",
  "build",
  "find",
  "api",
  "where"
 ],
 "ops_hint": ""
}"""


@dataclass(frozen=True)
class CapSpec:
    """Immutable description of one capability bit."""

    name: str
    domain: str
    desc: str
    handler: str
    safe: bool
    external: bool
    requires_params: bool
    params: Tuple[str, ...] = ()
    params_hint: str = ""
    multi_op: bool = False
    ops: Tuple[str, ...] = ()
    ops_hint: str = ""

    @property
    def gated(self) -> bool:
        """True when the registry marks this bit ``safe: false``.

        Gated does not mean "dangerous"; it means the action can change state
        that cannot be restored by running the inverse action.
        """
        return not self.safe

    @property
    def summary(self) -> str:
        """First clause of the description, for one-line listings."""
        for sep in ("\uff08", "\uff1b", "\u3002", ";"):
            if sep in self.desc:
                head = self.desc.split(sep, 1)[0].strip()
                if head:
                    return head
        return self.desc.strip()

    def as_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "domain": self.domain,
            "desc": self.desc,
            "handler": self.handler,
            "safe": self.safe,
            "gated": self.gated,
            "external": self.external,
            "requires_params": self.requires_params,
            "params": list(self.params),
            "params_hint": self.params_hint,
            "multi_op": self.multi_op,
            "ops": list(self.ops),
            "ops_hint": self.ops_hint,
        }


_data = json.loads(_RAW)

SPEC = CapSpec(
    name=_data["name"],
    domain=_data["domain"],
    desc=_data["desc"],
    handler=_data["handler"],
    safe=_data["safe"],
    external=_data["external"],
    requires_params=_data["requires_params"],
    params=tuple(_data["params"]),
    params_hint=_data["params_hint"],
    multi_op=_data["multi_op"],
    ops=tuple(_data["ops"]),
    ops_hint=_data["ops_hint"],
)
