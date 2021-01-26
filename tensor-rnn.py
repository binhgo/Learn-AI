from tensorflow.python.keras import Input
from tensorflow.python.keras.layers import Dense, Embedding, LSTM
from tensorflow.python.keras.models import Sequential
from tensorflow.keras import preprocessing as pp
from tensorflow.keras.layers.experimental.preprocessing import TextVectorization
from tensorflow import strings


def prepareData(dir):
    data = pp.text_dataset_from_directory(dir)
    return data.map(
        lambda text, label: (strings.regex_replace(text, '<br />', ' '), label),
    )


def runRNN():
    # Assumes you're in the root level of the dataset directory.
    # If you aren't, you'll need to change the relative paths here.
    train_data = prepareData('./train')
    test_data = prepareData('./test')

    for text_batch, label_batch in train_data.take(1):
        print(text_batch.numpy()[0])
        print(label_batch.numpy()[0])  # 0 = negative, 1 = positive

    model = Sequential()

    # ----- 1. INPUT
    # We need this to use the TextVectorization layer next.
    model.add(Input(shape=(1,), dtype="string"))

    # ----- 2. TEXT VECTORIZATION
    # This layer processes the input string and turns it into a sequence of
    # max_len integers, each of which maps to a certain token.
    max_tokens = 1000
    max_len = 100
    vectorize_layer = TextVectorization(
        # Max vocab size. Any words outside of the max_tokens most common ones
        # will be treated the same way: as "out of vocabulary" (OOV) tokens.
        max_tokens=max_tokens,
        # Output integer indices, one per string token
        output_mode="int",
        # Always pad or truncate to exactly this many tokens
        output_sequence_length=max_len,
    )

    # Call adapt(), which fits the TextVectorization layer to our text dataset.
    # This is when the max_tokens most common words (i.e. the vocabulary) are selected.
    train_texts = train_data.map(lambda text, label: text)
    vectorize_layer.adapt(train_texts)

    model.add(vectorize_layer)

    # ----- 3. EMBEDDING
    # This layer turns each integer (representing a token) from the previous layer
    # an embedding. Note that we're using max_tokens + 1 here, since there's an
    # out-of-vocabulary (OOV) token that gets added to the vocab.
    model.add(Embedding(max_tokens + 1, 128))

    # ----- 4. RECURRENT LAYER
    model.add(LSTM(64))

    # ----- 5. DENSE HIDDEN LAYER
    model.add(Dense(64, activation="relu"))

    # ----- 6. OUTPUT
    model.add(Dense(1, activation="sigmoid"))

    # Compile and train the model.
    model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
    model.fit(train_data, epochs=1)

    model.save_weights('rnn')


if __name__ == '__main__':
    runRNN()
