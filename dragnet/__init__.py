from dragnet.blocks import Blockifier, PartialBlock, BlockifyError
from dragnet import features
from dragnet.extractor import Extractor
from dragnet.util import load_pickled_model

_LOADED_MODELS = {}


def extract_content(html, encoding=None, as_blocks=False):
    if 'content' not in _LOADED_MODELS:
        _LOADED_MODELS['content'] = load_pickled_model(
            'kohlschuetter_readability_weninger_content_model.pkl.gz')
    return _LOADED_MODELS['content'].extract(html, encoding=encoding, as_blocks=as_blocks)


def extract_comments(html, encoding=None, as_blocks=False):
    if 'comments' not in _LOADED_MODELS:
        _LOADED_MODELS['comments'] = load_pickled_model(
            'kohlschuetter_readability_weninger_comments_model.pkl.gz')
    return _LOADED_MODELS['comments'].extract(html, encoding=encoding, as_blocks=as_blocks)


def extract_content_and_comments(html, encoding=None, as_blocks=False):
    if 'content_and_comments' not in _LOADED_MODELS:
        _LOADED_MODELS['content_and_comments'] = load_pickled_model(
            'kohlschuetter_readability_weninger_comments_content_model.pkl.gz')
    return _LOADED_MODELS['content_and_comments'].extract(html, encoding=encoding, as_blocks=as_blocks)
