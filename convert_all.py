import asyncio
from pathlib import Path
from opentele.tl import TelegramClient
from opentele.api import UseCurrentSession


async def convert_account(session_path: Path, output_base: Path):
    print(f"Processing account: {session_path}")

    client = TelegramClient(str(session_path))
    tdesk = await client.ToTDesktop(flag=UseCurrentSession)

    account_name = session_path.parent.name
    out_folder = output_base / f"tdata_{account_name}"
    out_folder.mkdir(parents=True, exist_ok=True)

    tdesk.SaveTData(str(out_folder))
    print(f"Saved tdata for {account_name} to {out_folder}")


async def main():
    accounts_dir = Path("accounts")
    output_dir = Path("output_tdata")

    session_files = list(accounts_dir.rglob("*.session"))

    tasks = []
    for session_path in session_files:
        tasks.append(convert_account(session_path, output_dir))

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
