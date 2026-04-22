from atcoder_links import parse_tasks
import pytest

def test_parse_tasks():
    html = """
    <div id="main-container">
        <table>
            <tbody>
                <tr>
                    <td><a href="/contests/abc300/tasks/abc300_a">A</a></td>
                    <td><a href="/contests/abc300/tasks/abc300_a">N-choice question</a></td>
                </tr>
                <tr>
                    <td><a href="/contests/abc300/tasks/abc300_b">B</a></td>
                    <td><a href="/contests/abc300/tasks/abc300_b">Same Map in the RPG World</a></td>
                </tr>
            </tbody>
        </table>
    </div>
    """
    tasks = parse_tasks(html)
    assert tasks == [
        {"label": "A", "title": "N-choice question", "url": "https://atcoder.jp/contests/abc300/tasks/abc300_a"},
        {"label": "B", "title": "Same Map in the RPG World", "url": "https://atcoder.jp/contests/abc300/tasks/abc300_b"},
    ]
