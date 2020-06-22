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

import hashlib
import time


class Block:

    def __init__(self, _index, _timestamp, _data, _previous_hash, _nonce=0):
        self.__index = _index
        self.__timestamp = _timestamp
        self.__data = _data
        self.__previous_hash = _previous_hash  # to ensure immutability of the entire blockchain
        self.__hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = str(self.index) + str(self.timestamp) + self.data
        sha.update(hash_str.encode('utf-8'))
        return sha.hexdigest()

    @property
    def index(self):
        return self.__index

    @property
    def timestamp(self):
        return self.__timestamp

    @property
    def data(self):
        return self.__data

    @property
    def previous_hash(self):
        return self.__previous_hash

    @property
    def hash(self):
        return self.__hash

    def __repr__(self):
        return "Block: \n" + "index= " + str(self.index) + \
               "\n" + "timestamp= " + str(self.timestamp) \
               + "\n" + "data= " + str(self.data) + \
               "\n" + "previous_hash= " + str(self.previous_hash) \
               + "\n" "hash= " + str(self.hash)


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

    @property
    def last_block(self):
        return self.chain[-1]

    def add_block(self, block: Block) -> bool:
        if block.hash == self.last_block.hash:
            print("->add_block: New block must have a unique code!")
            return False
        if self.last_block.hash != block.previous_hash \
                or block.data == "" or block.data is None:
            print("->add_block: Not valid data!")
            return False
        if block.index <= self.last_block.index:
            # raise Exception("New block index must be greater than previous")
            print("->add_block: New block index must be greater than previous!")
            return False

        self.chain.append(block)
        return True

    def print_chain(self):
        for item in self.chain:
            print("----------------------------")
            print(item)


def test_create_genesis_block():
    print("=============================================================================")
    print("->test_create_genesis_block: start")
    blockchain = BlockChain()  # create_genesis_block() is called in the constructor
    assert len(blockchain.chain) == 1
    assert blockchain.last_block.index == 0
    assert blockchain.last_block.data == "Genesis Block"
    assert blockchain.last_block.previous_hash == "0"
    # print(blockchain.last_block)
    print("->test_create_genesis_block: end")


def test_timestamp_format():
    print("=============================================================================")
    print("->test_timestamp_format: start")
    print("->test_timestamp_format: end")


def test_create_block_chain_1():
    print("=============================================================================")
    print("->test_create_block_chain_1: start")
    blockchain = BlockChain()

    # Case1 - all valid data
    print("case1:")
    block1 = Block(1, time.time(), "Block Data1", blockchain.last_block.hash)
    add_result = blockchain.add_block(block1)
    assert add_result
    assert blockchain.last_block.index == 1
    assert len(blockchain.chain) == 2

    # Case2 - index is lesser than the last block index
    print("case2:")
    block_wrong_index = Block(0, time.time(), "Block Data0", blockchain.last_block.hash)
    add_result = blockchain.add_block(block_wrong_index)
    assert add_result == False
    assert blockchain.last_block.index == 1
    assert len(blockchain.chain) == 2

    # Case3 - data is empty
    print("case3:")
    block_empty_data = Block(3, time.time(), "", blockchain.last_block.hash)
    add_result = blockchain.add_block(block_empty_data)
    assert add_result == False
    assert blockchain.last_block.index == 1
    assert len(blockchain.chain) == 2

    # Case4 - data is None
    print("case4:")
    block_none_data = Block(3, time.time(), "", blockchain.last_block.hash)
    add_result = blockchain.add_block(block_none_data)
    assert add_result == False
    assert blockchain.last_block.index == 1
    assert len(blockchain.chain) == 2

    # Case5 - not valid previous hash
    print("case5:")
    block_not_valid_prev_hash = Block(2, time.time(), "Block Data 2", "not valid prev hash")
    add_result = blockchain.add_block(block_not_valid_prev_hash)
    assert add_result == False
    assert blockchain.last_block.index == 1
    assert len(blockchain.chain) == 2

    blockchain.print_chain()
    print("->test_create_block_chain_1: end")


def test_create_block_chain_2():
    print("=============================================================================")
    print("->test_create_block_chain_2: start")
    blockchain = BlockChain()

    for i in range(1, 16):
        blockchain.add_block(Block(i, time.time(), "Block Data" + str(i), blockchain.last_block.hash))

    blockchain.print_chain()
    assert len(blockchain.chain) == 16  # 15 in range plus genesis
    block5 = blockchain.chain[5]
    # block5.index = 89 # Can not set the attribute
    assert block5.index == 5
    # blockchain.last_block = Block(2, time.time(), "Block Data 2", "not valid prev hash") # Can not set the attribute
    print("->test_create_block_chain_2: end")


def test():
    test_create_genesis_block()
    test_timestamp_format()
    test_create_block_chain_1()
    test_create_block_chain_2()


test()
