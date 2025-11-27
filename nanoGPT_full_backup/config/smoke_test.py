
# 极简测试配置
out_dir = 'out-smoke-test'
eval_interval = 2000 # 测试时不评估，为了快
eval_iters = 1
log_interval = 10

always_save_checkpoint = True

dataset = 'smoke_test'
batch_size = 4
block_size = 64 # 上下文长度

# 微型模型参数
n_layer = 2
n_head = 2
n_embd = 32
dropout = 0.0

learning_rate = 1e-3
max_iters = 50 # 只训练 50 步
lr_decay_iters = 50
min_lr = 1e-4 
beta2 = 0.99

warmup_iters = 0 
wandb_log = False # 不登录 wandb
