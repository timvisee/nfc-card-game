class_name Global

# Available mine IDs
const MINE_IDS = [1, 2, 3];

const API_URL: String = "http://localhost:8000/api";
const API_PATH_DASHBOARD: String = "/dashboard";

const WEBSOCKET_API_URL: String = "ws://localhost:8000/api/ws";

enum TeamId { TEAM1 = 1, TEAM2 = 2 }

enum MinerType { MINER1 = 1, MINER2 = 2, MINER3 = 3 };


# Get the current time in seconds.
static func now() -> int:
	@warning_ignore("integer_division")
	return Time.get_ticks_msec() / 1000;
