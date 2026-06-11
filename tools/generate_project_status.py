from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
STATUS_DOC = ROOT / "docs" / "project-status.md"

AUTO_START = "<!-- AUTO_STATUS_START -->"
AUTO_END = "<!-- AUTO_STATUS_END -->"

CHECK_ITEMS = {
    "PM / Architecture": {
        "owner": "정주헌",
        "files": [
            "README.md",
            "docs/architecture.md",
            "docs/team-task-guide.md",
            "docs/pre-run-checklist.md",
            "docs/troubleshooting.md",
            "docs/runbook.md",
            "docs/final-deliverables.md",
            "docs/review-checklist.md",
            "presentation/presentation-outline.md",
        ],
    },
    "Cloud Infrastructure": {
        "owner": "백서빈",
        "files": [
            "docs/network-design.md",
            "screenshots/cloud-infra/instance-list.png",
            "screenshots/cloud-infra/network-subnet.png",
            "screenshots/cloud-infra/security-group.png",
            "screenshots/cloud-infra/ssh-test.png",
        ],
    },
    "Server / Virtualization": {
        "owner": "이진욱",
        "files": [
            "docs/server-setup.md",
            "screenshots/server/os-info.png",
            "screenshots/server/docker-status.png",
            "screenshots/server/docker-ps.png",
            "screenshots/server/curl-result.png",
        ],
    },
    "Ansible Automation": {
        "owner": "조민석",
        "files": [
            "ansible/ansible.cfg",
            "ansible/inventory.ini",
            "ansible/site.yml",
            "docs/ansible-automation.md",
            "screenshots/ansible/ansible-version.png",
            "screenshots/ansible/inventory.png",
            "screenshots/ansible/ping-test.png",
            "screenshots/ansible/playbook-result.png",
            "screenshots/ansible/nginx-deploy-result.png",
        ],
    },
    "Monitoring / Backup / Validation": {
        "owner": "박재우",
        "files": [
            "scripts/health_check.sh",
            "scripts/backup.sh",
            "scripts/restore.md",
            "docs/validation-report.md",
            "screenshots/validation/health-check.png",
            "screenshots/validation/docker-status.png",
            "screenshots/validation/http-check.png",
            "screenshots/validation/backup-created.png",
            "screenshots/validation/recovery-result.png",
        ],
    },
}

def file_status(path_text: str) -> str:
    path = ROOT / path_text
    if path.exists() and path.is_file() and path.stat().st_size > 0:
        return "완료"
    if path.exists():
        return "파일 있음"
    return "미완료"

def status_icon(status: str) -> str:
    if status == "완료":
        return "✅"
    if status == "파일 있음":
        return "🟡"
    return "❌"

def build_status_markdown() -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    lines = []
    lines.append("# Project Status")
    lines.append("")
    lines.append(f"Last Updated: {now}")
    lines.append("")
    lines.append("## 1. 담당자별 진행 상태")
    lines.append("")
    lines.append("| 영역 | 담당자 | 완료 | 전체 | 진행률 | 상태 |")
    lines.append("|---|---|---:|---:|---:|---|")

    total_done = 0
    total_count = 0

    detail_sections = []

    for area, data in CHECK_ITEMS.items():
        owner = data["owner"]
        files = data["files"]

        done = 0
        detail_sections.append(f"## {area} - {owner}")
        detail_sections.append("")
        detail_sections.append("| 파일 | 상태 |")
        detail_sections.append("|---|---|")

        for file_path in files:
            status = file_status(file_path)
            icon = status_icon(status)

            if status == "완료":
                done += 1

            detail_sections.append(f"| {file_path} | {icon} {status} |")

        count = len(files)
        percent = round((done / count) * 100) if count else 0

        total_done += done
        total_count += count

        if percent == 100:
            area_status = "✅ 완료"
        elif percent >= 50:
            area_status = "🟡 진행 중"
        else:
            area_status = "❌ 미흡"

        lines.append(f"| {area} | {owner} | {done} | {count} | {percent}% | {area_status} |")

        detail_sections.append("")

    total_percent = round((total_done / total_count) * 100) if total_count else 0

    lines.append("")
    lines.append("## 2. 전체 진행률")
    lines.append("")
    lines.append("| 완료 | 전체 | 진행률 |")
    lines.append("|---:|---:|---:|")
    lines.append(f"| {total_done} | {total_count} | {total_percent}% |")
    lines.append("")
    lines.append("## 3. 상세 파일 상태")
    lines.append("")
    lines.extend(detail_sections)

    return "\n".join(lines).strip() + "\n"

def build_readme_auto_section(status_markdown: str) -> str:
    lines = status_markdown.splitlines()

    table_start = None
    table_end = None

    for index, line in enumerate(lines):
        if line.startswith("| 영역 | 담당자 |"):
            table_start = index
        if table_start is not None and line.startswith("## 2. 전체 진행률"):
            table_end = index
            break

    status_table = "\n".join(lines[table_start:table_end]).strip() if table_start is not None else ""

    total_section = []
    capture = False
    for line in lines:
        if line.startswith("## 2. 전체 진행률"):
            capture = True
        elif line.startswith("## 3. 상세 파일 상태"):
            break

        if capture:
            total_section.append(line)

    total_text = "\n".join(total_section).strip()

    return f"""## 자동 생성 프로젝트 상태

아래 상태는 팀원이 파일을 push할 때 자동으로 갱신된다.

{total_text}

## 담당자별 진행 상태

{status_table}

상세 상태는 [Project Status](./docs/project-status.md) 문서에서 확인한다.
"""

def update_readme(auto_section: str) -> None:
    if not README.exists():
        raise FileNotFoundError("README.md not found")

    content = README.read_text(encoding="utf-8")

    if AUTO_START not in content or AUTO_END not in content:
        content += f"\n\n{AUTO_START}\n{auto_section}\n{AUTO_END}\n"
    else:
        before = content.split(AUTO_START)[0]
        after = content.split(AUTO_END)[1]
        content = f"{before}{AUTO_START}\n{auto_section}\n{AUTO_END}{after}"

    README.write_text(content, encoding="utf-8")

def main() -> None:
    status_markdown = build_status_markdown()
    STATUS_DOC.write_text(status_markdown, encoding="utf-8")

    auto_section = build_readme_auto_section(status_markdown)
    update_readme(auto_section)

    print("Project status generated successfully.")

if __name__ == "__main__":
    main()
