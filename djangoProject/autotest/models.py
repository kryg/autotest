# -*- coding: utf-8; show-trailing-whitespace: t -*-

from django.db.models.loading import get_models
from django.utils.functional import curry
from lettuce.django.steps.models import _MODEL_EXISTS, models_exist, STEP_PREFIX
from lettuce import *


def _models_generator():
    """
    Build a hash of model verbose names to models
    """
    for model in get_models():
        yield (unicode(model._meta.object_name), model)


def get_model(model):
    """
    Convert a model's verbose name to the model class. This allows us to
    use the models verbose name in steps.
    """

    name = model.lower()
    model = MODELS.get(model, None)

    assert model, "Could not locate model by name '%s'" % name

    return model


@step(STEP_PREFIX + r'(?:an? )?([A-Z][a-z0-9_ ]*) should be present in the database')
def models_exist_generic(step, model):
    """
    And objectives should be present in the database:
    | description      |
    | Make a mess      |
    """

    model = get_model(model)

    try:
        func = _MODEL_EXISTS[model]
    except KeyError:
        func = curry(models_exist, model)

    func(step)

MODELS = dict(_models_generator())
