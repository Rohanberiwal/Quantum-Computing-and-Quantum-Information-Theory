import hashlib
import math

def sha256(data):
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def build_merkle_tree(transactions):
    tree = []
    current_level = [sha256(tx) for tx in transactions]
    tree.append(current_level)
    
    while len(current_level) > 1:
        next_level = []
        if len(current_level) % 2 == 1:
            current_level.append(current_level[-1])
        for i in range(0, len(current_level), 2):
            combined = current_level[i] + current_level[i+1]
            next_level.append(sha256(combined))
        tree.append(next_level)
        current_level = next_level
    
    return tree

def get_merkle_root(tree):
    return tree[-1][0]

def get_merkle_branch(tree, index):
    branch = []
    for level in tree[:-1]:
        if len(level) % 2 == 1:
            level = level + [level[-1]]
        sibling_index = index ^ 1
        branch.append(level[sibling_index])
        index = index // 2
    return branch

def verify_transaction(tx, branch, merkle_root, index):
    current_hash = sha256(tx)
    for sibling in branch:
        if index % 2 == 0:
            current_hash = sha256(current_hash + sibling)
        else:
            current_hash = sha256(sibling + current_hash)
        index = index // 2
    return current_hash == merkle_root

if __name__ == "__main__":
    transactions = [
        "Transaction 1: Alice pays Bob 10 BTC",
        "Transaction 2: Bob pays Charlie 5 BTC",
        "Transaction 3: Charlie pays Dave 2 BTC",
        "Transaction 4: Dave pays Eve 1 BTC",
        "Transaction 5: Eve pays Frank 0.5 BTC"
    ]

    merkle_tree = build_merkle_tree(transactions)
    merkle_root = get_merkle_root(merkle_tree)
    print("Merkle Tree Levels:")
    for level_num, level in enumerate(merkle_tree):
        print(f"Level {level_num}: {level}")
    print("\nMerkle Root:", merkle_root)

    tx_index = 2
    tx_to_verify = transactions[tx_index]
    branch = get_merkle_branch(merkle_tree, tx_index)
    print("\nMerkle Branch for Transaction at index", tx_index, ":", branch)
    
    is_valid = verify_transaction(tx_to_verify, branch, merkle_root, tx_index)
    print("\nVerification of the transaction:", is_valid)
 
