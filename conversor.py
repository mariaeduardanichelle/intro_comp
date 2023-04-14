{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPalY8+I0KbzUUqTqbKFNPb"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mCDNBbkooT_4",
        "outputId": "c9d04544-a44f-4a60-8ebc-162a857de283"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um número: 24\n",
            "Digite a base: 8\n",
            "20\n"
          ]
        }
      ],
      "source": [
        "num = str(input('Digite um número: '))\n",
        "base = int(input('Digite a base: '))\n",
        "conv = list()\n",
        "nnum = list()\n",
        "cnum = 0\n",
        "for n in num:\n",
        "  conv.append(int(n))\n",
        "conv.reverse()\n",
        "for i, n in enumerate(conv):\n",
        "  nnum.append(n * base ** i)\n",
        "for n in nnum:\n",
        "  cnum += n\n",
        "print(cnum)"
      ]
    }
  ]
}