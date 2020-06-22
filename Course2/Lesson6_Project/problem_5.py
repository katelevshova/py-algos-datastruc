"""
TASK5:
Blockchain

A Blockchain is a sequential chain of records, similar to a linked list.
Each block contains some information and how it is connected related to the other blocks in the chain.
Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data.
For our blockchain we will be using a SHA-256 hash, the Greenwich Mean Time when the block was created,
and text strings as the data.

Use your knowledge of linked lists and hashing to create a blockchain implementation.

"""
"""
NOTE:
A blockchain is essentially a linked list that contains ordered data, 
with a few constraints such as:

    Blocks can’t be modified once added; in other words, it is append only.
    There are specific rules for appending data to it.
    Its architecture is distributed.
"""
# USED sources: https://www.activestate.com/blog/how-to-build-a-blockchain-in-python/

import hashlib
import time


class Block:

    def __init__(self, _index, _timestamp, _data, _previous_hash, _nonce=0):
        self.index = _index
        self.timestamp = _timestamp
        self.data = _data
        self.previous_hash = _previous_hash  # to ensure immutability of the entire blockchain
        self.hash = self.calc_hash()
        self.nonce = _nonce  # value that starts with a certain number of zero bits when hashed

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = "We are going to encode this string of data!".encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def __repr__(self):
        return "Block: \n" + \
               "index= " + str(self.index) + "\n" \
                                             "timestamp= " + str(self.timestamp) + "\n" \
                                                                                   "data= " + str(self.data) + "\n" \
                                                                                                               "previous_hash= " + str(
            self.previous_hash) + "\n" \
                                  "hash= " + str(self.hash)


class BlockChain:

    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        Is used to initialize the blockchain.
        Creates an initial block with an index of 0 and a previous hash of 0.
        """
        genesis_block = Block(0, time.time(), "Genesis Block", "0")
        self.chain.append(genesis_block)

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, block: Block) -> bool:
        if self.get_last_block().hash != block.previous_hash or block.data == "":
            return False
        if block.index <= self.get_last_block().index:
            # raise Exception("New block index must be greater than previous")
            print("New block index must be greater than previous!")
            return False
        self.chain.append(block)
        return True


def test_create_genesis_block():
    print("->test_create_genesis_block: start")
    blockchain = BlockChain()  # create_genesis_block() is called in the constructor
    assert len(blockchain.chain) == 1
    assert blockchain.get_last_block().index == 0
    assert blockchain.get_last_block().data == "Genesis Block"
    assert blockchain.get_last_block().previous_hash == "0"
    # print(blockchain.get_last_block())
    print("->test_create_genesis_block: end")


def test_create_block_chain_1():
    print("->test_create_block_chain_1: start")
    blockchain = BlockChain()
    print("->test_create_block_chain_1: end")


def test():
    test_create_genesis_block()
    test_create_block_chain_1()


test()
