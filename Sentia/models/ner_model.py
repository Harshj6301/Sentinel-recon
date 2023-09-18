from flair.models import SequenceTagger
from flair.data import Sentence

def ner(text):

    ENTITY = []
    TAG = []

    # Load the pre-trained NER model
    tagger = SequenceTagger.load('ner')
    text = text
    # Create a Sentence object
    sentence = Sentence(text)

    # Run NER on the sentence
    tagger.predict(sentence)

    for entity in sentence.get_spans('ner'):
        ENTITY.append(entity.text)
        TAG.append(entity.tag)

    return ENTITY, TAG
    #df = pd.DataFrame({'Entity':ENTITY,'Tag':TAG})
    #df