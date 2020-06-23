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

import datetime
import hashlib


class Block:

    def __init__(self, _index, _timestamp, _data, _previous_hash, _nonce=0):
        self.__index = _index
        self.__timestamp = _timestamp
        self.__data = _data
        self.__previous_hash = _previous_hash  # to ensure immutability of the entire blockchain
        self.nonce = _nonce
        self.hash = self.calc_hash()

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

    @hash.setter
    def hash(self, _hash):
        self.__hash = _hash

    def __repr__(self):
        return "Block: \nindex= " + str(self.index) + \
               "\ntimestamp= " + str(self.timestamp) + \
               "\ndata= " + str(self.data) + \
               "\nprevious_hash= " + str(self.previous_hash) + \
               "\nhash= " + str(self.hash)


class BlockChain:
    difficulty = 2

    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        Is used to initialize the blockchain.
        Creates an initial block with an index of 0 and a previous hash of 0.
        """
        genesis_block = Block(0, datetime.datetime.now(datetime.timezone.utc), "Genesis Block", "0")
        self.chain.append(genesis_block)

    @property
    def last_block(self):
        return self.chain[-1]

    def proof_of_work(self, block):
        computed_hash = block.calc_hash()
        while not computed_hash.startswith('0' * BlockChain.difficulty):
            block.nonce += 1
            computed_hash = block.calc_hash()
        return computed_hash

    def add_block(self, block: Block, proof) -> bool:
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
        if not self.is_valid_proof(block, proof):
            return False
        block.hash = proof
        self.chain.append(block)
        return True

    def is_valid_proof(self, block, block_hash):
        return (block_hash.startswith('0' * BlockChain.difficulty) and
                block_hash == block.calc_hash())

    def mine(self) -> int:
        block = Block(self.last_block.index+1,
                      datetime.datetime.now(datetime.timezone.utc),
                      "New block data",
                      self.last_block.hash)
        proof = self.proof_of_work(block)
        self.add_block(block, proof)
        return block.index

    def print_chain(self):
        for item in self.chain:
            print("----------------------------")
            print(item)


# TEST CASES: start----------------------------------------------
def test_create_genesis_block():
    print("=============================================================================")
    print("->test_create_genesis_block: start")
    blockchain = BlockChain()  # create_genesis_block() is called in the constructor
    assert len(blockchain.chain) == 1
    assert blockchain.last_block.index == 0
    assert blockchain.last_block.data == "Genesis Block"
    assert blockchain.last_block.previous_hash == "0"
    print(blockchain.last_block)
    print("->test_create_genesis_block: end")


def test_create_block_chain_1():
    print("=============================================================================")
    print("->test_create_block_chain_1: start")
    blockchain = BlockChain()

    # Case1 - all valid data
    print("case1:")
    block1 = Block(1, datetime.datetime.now(datetime.timezone.utc), "Block Data1", blockchain.last_block.hash)
    add_result = blockchain.add_block(block1)
    assert add_result
    assert blockchain.last_block.index == 1
    assert len(blockchain.chain) == 2

    # Case2 - index is lesser than the last block index
    print("case2:")
    block_wrong_index = Block(0, datetime.datetime.now(datetime.timezone.utc), "Block Data0",
                              blockchain.last_block.hash)
    add_result = blockchain.add_block(block_wrong_index)
    assert add_result == False
    assert blockchain.last_block.index == 1
    assert len(blockchain.chain) == 2

    # Case3 - data is empty
    print("case3:")
    block_empty_data = Block(3, datetime.datetime.now(datetime.timezone.utc), "", blockchain.last_block.hash)
    add_result = blockchain.add_block(block_empty_data)
    assert add_result == False
    assert blockchain.last_block.index == 1
    assert len(blockchain.chain) == 2

    # Case4 - data is None
    print("case4:")
    block_none_data = Block(3, datetime.datetime.now(datetime.timezone.utc), "", blockchain.last_block.hash)
    add_result = blockchain.add_block(block_none_data)
    assert add_result == False
    assert blockchain.last_block.index == 1
    assert len(blockchain.chain) == 2

    # Case5 - not valid previous hash
    print("case5:")
    block_not_valid_prev_hash = Block(2, datetime.datetime.now(datetime.timezone.utc), "Block Data 2",
                                      "not valid prev hash")
    add_result = blockchain.add_block(block_not_valid_prev_hash)
    assert add_result == False
    assert blockchain.last_block.index == 1
    assert len(blockchain.chain) == 2

    blockchain.print_chain()
    print("->test_create_block_chain_1: end")


def test():
    test_create_genesis_block()
   # test_create_block_chain_1()


# TEST CASES: end----------------------------------------------

test()
