#!/usr/bin/env python
# coding: utf-8

# In[1]:

import torch
import torch.nn as nn
import torch.optim as optim
from tqdm import tqdm 

def train_model(model, train_loader, val_loader, device="cpu", epochs=10, lr=0.001):
    """
    Train a model with CrossEntropyLoss and Adam optimizer.
    Args:
        model: PyTorch model
        train_loader: DataLoader for training
        val_loader: DataLoader for validation
        device: "cpu" or "cuda"
        epochs: Number of training epochs
        lr: Learning rate
    """
    model.to(device)
    loss_fn = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=lr)

    for epoch in range(epochs):
        model.train()
        total_loss = 0.0
        progress_bar = tqdm(train_loader, desc=f"Epoch {epoch+1}/{epochs}", leave=False)

        for inputs, targets in progress_bar:
            inputs, targets = inputs.to(device), targets.to(device)

            optimizer.zero_grad()
            output = model(inputs)
            loss = loss_fn(output, targets)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        
        avg_loss = total_loss / len(train_loader)
        print(f"Epoch {epoch+1}/{epochs}, Training Loss: {avg_loss:.4f}")

        # Validation step
        model.eval()
        val_loss = 0.0
        correct = 0
        total = 0
        
        with torch.no_grad():
            for inputs, targets in val_loader:
                inputs, targets = inputs.to(device), targets.to(device)
                output = model(inputs)
                val_loss += loss_fn(output, targets).item()
                
                # Compute accuracy
                _, predicted = torch.max(output, 1)
                total += targets.size(0)
                correct += (predicted == targets).sum().item()
        
        avg_val_loss = val_loss / len(val_loader)
        val_accuracy = correct / total * 100
        print(f"Epoch {epoch+1}/{epochs}, Validation Loss: {avg_val_loss:.4f}, Validation Accuracy: {val_accuracy:.2f}%")

    print("Training Complete!")

# In[ ]:




