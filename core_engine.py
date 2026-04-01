dynamic_scale_factor = 0.82 + 0.03 * (1.0 - layer_ratio)

exp = 0.75 + 0.2 * (1.0 - layer_ratio)
weight_vec = (1.0 / (importance_vec + 1e-6)) ** exp
