# The entire Snakemake-facing wrapper. It is GENERIC (one file dispatches every
# step) and UNCHANGED by the sensitivity-study feature: it only ever receives
# an already-merged config dict for one ensemble member. It runs inside the
# rule's own conda env and depends only on `cedalion_workflows` (dependency-free), so
# it works identically whether the step lives in corelib, userlib, or anywhere.

from cedalion_workflows import resolve, bind_config

if "snakemake" not in globals():
    raise RuntimeError("This script must be run through Snakemake.")

func = resolve(snakemake.params.func)                 # noqa: F821 (Snakemake-injected)

cfg = dict(snakemake.params.config)                   # noqa: F821  algorithmic params
cfg.update(dict(snakemake.input.items()))             # noqa: F821  named inputs  -> args
cfg.update(dict(snakemake.output.items()))            # noqa: F821  named outputs -> args

bound = bind_config(func, cfg)                        # validate against the signature
func(*bound.args, **bound.kwargs)
