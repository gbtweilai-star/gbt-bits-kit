# bits_kit

**One capability bit from GBT V8, packaged standalone.** No. 13 of 341,
`creation` domain (Creation).

<p>
<img alt="python" src="https://img.shields.io/badge/python-3.9%2B-blue">
<img alt="license" src="https://img.shields.io/badge/license-MIT-green">
<img alt="deps" src="https://img.shields.io/badge/runtime%20dependencies-0-brightgreen">
</p>

> **动效组件图鉴的口**（人话 → react-bits 哪个组件 · 干什么 · **源码在哪 · 会不会联网 · 依赖什么**）。素材：`DavidHDev/react-bits`（**MIT + Commons Clause v1.0** · ★49005 · 216 组件 · 5 类：Animations 39 / Backgrounds 62 / Components 48 / Micro 34 / TextAnimations 33）落 `_upstream/react-bits`。常用说法：动画 / 背景 / 文字动画 / 微交互 / 手风琴 / 画廊 / 卡片 / 光标跟随 / 粒子 / 网格 / 渐变 / 流光 / 毛玻璃 / 滚动 / 计数 / 故障 / 极光 / 波浪 / 液态 / 三维 / 音频 / 拖拽 / 轮播 / 开关 / 加载 / 翻牌 / 解密 / 描边 / 磁性。op=status/build/find/api/where：`build` 扫 `src/content`（**盘上目录是真相**）提 名·类目·说明（取自官方 `public/llms.txt`）·源码路径·注册表·依赖·**联网标**，落 `store/bits_kit/index.jsonl`（只追加），并把「清单与盘上对不上的地方」如实带出来；`find` 人话取候选（**命中 0 就是 0**，可 `only_offline=true` 只看不联网的）；`api` 按准确名取一条。🔴 铁律：**只读 · 零执行 · 不搬成品**（许可禁止再分发/移植）· **不碰 `public/rbp/**`**（付费版 Pro）· **不改 `_upstream/react-bits/**` 一个字节** · 说明只取原文，取不到留空。

That description is copied verbatim from the registry. `tests/test_spec.py` pins it,
so documentation drift fails the build instead of shipping quietly.

## What this package actually is

It is the **contract** for one capability: its name, its parameters, the values it
accepts, and whether it can change state that cannot be restored. It is not the
implementation — that lives in the runtime this bit was extracted from.

So `run()` goes through a narrow `Backend` protocol, and the default backend is a
stub that **says so**:

```
status="validated"   backend="stub"   data={"executed": false}
```

Never `status="ok"`. A stub that reports success is worse than no stub, because the
caller stops looking for the real thing.

## Install

```bash
git clone https://github.com/gbtweilai-star/gbt-bits-kit.git
cd gbt-bits-kit
python -m pip install -e ".[dev]"
```

## Use

```bash
python -m gbt_bits_kit info                  # capability card
python -m gbt_bits_kit spec --json           # machine-readable contract
python -m gbt_bits_kit check --payload '{}'
python -m gbt_bits_kit run   --payload '{}'
```

Real `info` output from this machine:

```text
bits_kit  (creation)  v1.0.0
----------------------------------------
**动效组件图鉴的口**（人话 → react-bits 哪个组件 · 干什么 · **源码在哪 · 会不会联网 · 依赖什么**）。素材：`DavidHDev/react-bits`（**MIT + Commons Clause v1.0** · ★49005 · 216 组件 · 5 类：Animations 39 / Backgrounds 62 / Components 48 / Micro 34 / TextAnimations 33）落 `_upstream/react-bits`。常用说法：动画 / 背景 / 文字动画 / 微交互 / 手风琴 / 画廊 / 卡片 / 光标跟随 / 粒子 / 网格 / 渐变 / 流光 / 毛玻璃 / 滚动 / 计数 / 故障 / 极光 / 波浪 / 液态 / 三维 / 音频 / 拖拽 / 轮播 / 开关 / 加载 / 翻牌 / 解密 / 描边 / 磁性。op=status/build/find/api/where：`build` 扫 `src/content`（**盘上目录是真相**）提 名·类目·说明（取自官方 `public/llms.txt`）·源码路径·注册表·依赖·**联网标**，落 `store/bits_kit/index.jsonl`（只追加），并把「清单与盘上对不上的地方」如实带出来；`find` 人话取候选（**命中 0 就是 0**，可 `only_offline=true` 只看不联网的）；`api` 按准确名取一条。🔴 铁律：**只读 · 零执行 · 不搬成品**（许可禁止再分发/移植）· **不碰 `public/rbp/**`**（付费版 Pro）· **不改 `_upstream/react-bits/**` 一个字节** · 说明只取原文，取不到留空。

gated      : False
external   : False
multi-op   : True
params     : (none)
values     : status, build, find, api, where
```

Wire a real implementation:

```python
from gbt_bits_kit import run

class MyBackend:
    name = "my-backend"
    def invoke(self, cap, payload):
        return {"cap": cap, "handled": sorted(payload)}

result = run({}, backend=MyBackend())
assert result.status == "ok"
```

## Parameters

| name | required | notes |
|---|---|---|
| — | no | the registry declares no required parameters |

Registry hint (`params_hint`): (empty)

**注册表登记的取值 / 子动作（5 个）**：`status`、`build`、`find`、`api`、`where`

Types are deliberately absent: the registry does not declare them, and an invented
type is worse than no type, because callers believe it.

## Boundaries

- Not gated: the registry marks this bit `safe: true`.
- No external service dependency declared.
- Multi-op (`multi_op: true`): several sub-actions share one name — read `op` before calling.
- No implementation ships here. Bring a backend; the protocol is one method.

## What this is not

Not a wrapper around a hosted API. Not a model. Not a promise that calling it does
anything on its own. It is the typed seam plus the validation, which is the part that
stays correct even when the implementation changes.

## Tests

```bash
python -m pytest
```

```text
20 passed, 3 skipped in 0.11s
```

## Provenance

| field | value |
|---|---|
| capability | `bits_kit` |
| domain | `creation` |
| handler | `bits_kit` |
| safe | `True` (gated = `False`) |
| external | `False` |
| atlas page | [creation/bits_kit](https://github.com/gbtweilai-star/gbt-caps/blob/main/caps/creation/bits_kit.md) |
| full index | [https://github.com/gbtweilai-star/gbt-caps](https://github.com/gbtweilai-star/gbt-caps) |

The parent README says 348 capabilities; an AST pass over the registry enumerates
`341 + 0 unimplemented + 0 disabled = 341`. The extra 7 are historical duplicates.
Numbering here follows 341 and matches the `gbt-caps` index one-to-one.

## License

MIT.
