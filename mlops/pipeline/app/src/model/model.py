import torch
import torch.nn as nn
from pathlib import Path
from model.vocab import open_json

file_path = "./model/naver_vocab.json"
word_to_index = open_json(file_path)

class TextClassifier(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim, output_dim):
        super(TextClassifier, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.lstm = nn.LSTM(embedding_dim, hidden_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        embedded = self.embedding(x)

        lstm_out, (hidden, cell) = self.lstm(embedded)

        last_hidden = hidden.squeeze(0)
        logits = self.fc(last_hidden)
        return logits
    
model = TextClassifier(len(word_to_index), embedding_dim=100, hidden_dim=128, output_dim=2)

model.load_state_dict(
    torch.load(
        Path(__file__).parent.absolute() / "artifact" / "best_model_checkpoint.pth",
        map_location= torch.device("cpu"),
    )
)

model.eval()