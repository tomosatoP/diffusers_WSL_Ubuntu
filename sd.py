#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
import torch
from diffusers import StableDiffusionPipeline as Pipeline
from diffusers import EulerAncestralDiscreteScheduler as Scheduler


torch.backends.cuda.matmul.allow_tf32 = True

MODEL_ID = "model/stabilityai/stable-diffusion-2-1"
DEVICE = "cuda"

pipe = Pipeline.from_pretrained(MODEL_ID)
pipe.scheduler = Scheduler.from_config(pipe.scheduler.config)
pipe = pipe.to(DEVICE)

PROMPT = "a photo of an astronaut riding a horse on mars"
NPROMPT = "worst quality"
image = pipe(PROMPT, negative_prompt=NPROMPT).images[0]

image.save(f"img_{datetime.now().strftime('%Y%m%d-%H%M%S')}.png")
