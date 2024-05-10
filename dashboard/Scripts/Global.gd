class_name Global

enum MinerType { MINER1, MINER2, MINER3 };


static func miner_type_index(type: MinerType):
	match randi() % 3:
		MinerType.MINER1:
			return 0;
		MinerType.MINER2:
			return 1;
		MinerType.MINER3:
			return 2;
		_:
			assert(false, "unknown miner type");
