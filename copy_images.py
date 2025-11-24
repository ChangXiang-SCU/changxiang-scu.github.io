import shutil
import os

brain_dir = r"C:\Users\Chang\.gemini\antigravity\brain\bad72083-ca90-49d8-ad00-5917403ad728"
target_dir = r"c:\Users\Chang\changxiang-scu.github.io\images"

mapping = {
    "c_users_chang_changxiang_scu_github_io_images_paper_2021_iceb_png_1763978286723.png": "paper_2021_iceb.png",
    "c_users_chang_changxiang_scu_github_io_images_paper_2022_iceb_png_1763978254912.png": "paper_2022_iceb.png",
    "c_users_chang_changxiang_scu_github_io_images_paper_2023_chi_png_1763978371142.png": "paper_2023_chi.png",
    "c_users_chang_changxiang_scu_github_io_images_paper_2024_chi_png_1763978070876.png": "paper_2024_chi.png",
    "c_users_chang_changxiang_scu_github_io_images_paper_2025_aspire_png_1763978092973.png": "paper_2025_aspire.png",
    "c_users_chang_changxiang_scu_github_io_images_paper_2025_autoui_png_1763978120132.png": "paper_2025_autoui.png",
    "c_users_chang_changxiang_scu_github_io_images_paper_2025_aaai_png_1763977854924.png": "paper_2025_aaai.png"
}

for src_name, dest_name in mapping.items():
    src_path = os.path.join(brain_dir, src_name)
    dest_path = os.path.join(target_dir, dest_name)
    if os.path.exists(src_path):
        shutil.copy(src_path, dest_path)
        print(f"Copied {src_name} -> {dest_name}")
    else:
        print(f"Source not found: {src_path}")
