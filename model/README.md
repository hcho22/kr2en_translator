---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: hcho22/opus-mt-ko-en-finetuned-en-to-kr
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# hcho22/opus-mt-ko-en-finetuned-en-to-kr

This model is a fine-tuned version of [Helsinki-NLP/opus-mt-ko-en](https://huggingface.co/Helsinki-NLP/opus-mt-ko-en) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 2.5856
- Validation Loss: 2.0437
- Train Bleu: 2.0518
- Train Gen Len: 20.8110
- Epoch: 0

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': 2e-05, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-07, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Train Bleu | Train Gen Len | Epoch |
|:----------:|:---------------:|:----------:|:-------------:|:-----:|
| 2.5856     | 2.0437          | 2.0518     | 20.8110       | 0     |


### Framework versions

- Transformers 4.24.0
- TensorFlow 2.9.2
- Datasets 2.6.1
- Tokenizers 0.13.2
