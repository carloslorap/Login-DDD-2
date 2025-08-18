from flask import Blueprint, render_template
from app.decorators.protection import login_required, roles_required
from app.core.roles import ROLE_ADMIN
from app.infrastructure.repositories.dashboard.dashboard_repository import DashboardStatsRepository

dashboard_bp = Blueprint("dashboard", __name__)  # ya lo tienes

_stats_repo = DashboardStatsRepository()

@dashboard_bp.route("/", methods=["GET"])
@login_required
@roles_required(ROLE_ADMIN)  # ambos roles lo pueden ver
def dashboard():
    stats = _stats_repo.get_stats()
    return render_template("dashboard.html", stats=stats)