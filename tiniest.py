#!/usr/bin/env python
# encoding: utf-8

"""
@author: david
@time: 9/19/17 7:36 PM
五十行python代码构建小型区块链
http://www.cnblogs.com/fangbei/p/build-blockchain.html
Let's Build the Tiniest Blockchain

200 行代码实现一个简单的区块链
http://blog.jobbole.com/110860/
"""

import hashlib as hasher
import datetime as date


# Define what a Snakecoin block is
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        return _calculate_hash_for_block(self)
        # sha = hasher.sha256()
        # sha.update(str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash))
        # return sha.hexdigest()


# Generate genesis block
def create_genesis_block():
    # Manually construct a block with
    # index zero and arbitrary previous hash
    return Block(0, date.datetime.now(), "Genesis Block", "0")


# 块的生成
# Generate all later blocks in the blockchain
def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "Hey! I'm block " + str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)


# 确认块的完整性
def is_valid_new_block(newBlock, previousBlock):
    '''
    在任何时候都必须能确认一个区块或者一整条链的区块是否完整。
    在我们从其他节点接收到新的区块，并需要决定接受或拒绝它们时，这一点尤为重要。
    '''
    if previousBlock.index + 1 != newBlock.index:
        print('invalid index');
        return False;
    elif previousBlock.hash != newBlock.previousHash:
        print('invalid previoushash');
        return False;
    elif _calculate_hash_for_block(newBlock) != newBlock.hash:
        print('invalid hash: ' + _calculate_hash_for_block(newBlock) + ' ' + newBlock.hash);
        return False;
    return True


# 块哈希
def _calculate_hash_for_block(block):
    sha = hasher.sha256()
    sha.update(str(block.index) + str(block.timestamp) + str(block.data) + str(block.previous_hash))
    return sha.hexdigest()
def replaceChain (newBlocks):
    if isValidChain(newBlocks) && newBlocks.length > blockchain.length:
        print('Received blockchain is valid. Replacing current blockchain with received blockchain');
        blockchain = newBlocks;
        broadcast(responseLatestMsg());
    } else {
        print('Received blockchain invalid');
    }
};

if __name__ == '__main__':

    # Create the blockchain and add the genesis block
    blockchain = [create_genesis_block()]
    previous_block = blockchain[0]

    # How many blocks should we add to the chain
    # after the genesis block
    num_of_blocks_to_add = 20

    # Add blocks to the chain
    for i in range(0, num_of_blocks_to_add):
        block_to_add = next_block(previous_block)
        blockchain.append(block_to_add)
        previous_block = block_to_add
        # Tell everyone about it!
        print "Block #{} has been added to the blockchain!".format(block_to_add.index)
    print "Hash: {}\n".format(block_to_add.hash)
