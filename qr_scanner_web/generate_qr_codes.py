#!/usr/bin/env python3
"""
Standalone QR code generator for team scanner
Run this to generate printable QR codes without starting the server
"""

import qrcode
import zipfile
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

def create_qr_code(team_letter):
    """Generate a QR code for a team"""
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(f"TEAM_{team_letter}")
    qr.make(fit=True)
    return qr.make_image(fill_color="black", back_color="white")

def create_printable_qr(team_letter, add_label=True):
    """Create a printable QR code with team label"""
    qr_img = create_qr_code(team_letter)
    
    if not add_label:
        return qr_img
    
    # Create larger image with label
    qr_size = qr_img.size[0]
    label_height = 100
    
    # Create new image with extra space for label
    img = Image.new('RGB', (qr_size, qr_size + label_height), color='white')
    
    # Paste QR code
    img.paste(qr_img, (0, label_height))
    
    # Add team label
    draw = ImageDraw.Draw(img)
    try:
        # Try to use a larger font if available
        font = ImageFont.truetype("arial.ttf", 60)
    except:
        # Fall back to default font
        font = ImageFont.load_default()
    
    text = f"TEAM {team_letter}"
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_x = (qr_size - text_width) // 2
    text_y = 20
    
    draw.text((text_x, text_y), text, fill='black', font=font)
    
    return img

def main():
    teams = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    
    # Create output directory
    output_dir = Path("qr_codes_generated")
    output_dir.mkdir(exist_ok=True)
    
    print("🎯 Generating QR Codes...")
    print(f"📁 Output directory: {output_dir.absolute()}")
    print()
    
    # Generate individual QR codes
    for team in teams:
        qr_img = create_printable_qr(team, add_label=True)
        file_path = output_dir / f"TEAM_{team}_PRINTABLE.png"
        qr_img.save(file_path, dpi=(300, 300))
        print(f"✅ Generated: TEAM_{team}_PRINTABLE.png")
    
    print()
    print("📦 Creating ZIP file...")
    
    # Create ZIP file with all QR codes
    zip_path = Path("team_qr_codes.zip")
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for team in teams:
            file_path = output_dir / f"TEAM_{team}_PRINTABLE.png"
            zipf.write(file_path, arcname=f"TEAM_{team}_PRINTABLE.png")
    
    print(f"✅ ZIP created: {zip_path}")
    print()
    print("📋 Summary:")
    print(f"   • 7 QR codes generated")
    print(f"   • Each code contains: TEAM_[A-G]")
    print(f"   • Location: {output_dir.absolute()}")
    print()
    print("🖨️  Next steps:")
    print("   1. Download team_qr_codes.zip")
    print("   2. Extract all PNG files")
    print("   3. Print each PNG at high quality (300 DPI)")
    print("   4. Laminate for durability")
    print()

if __name__ == "__main__":
    main()
